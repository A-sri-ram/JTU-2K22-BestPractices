from typing import List, Tuple
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User

from restapi.models import Category, Groups, UserExpense, Expenses
from typing import Tuple
import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        """ 
        Creates and user
        """
        user = User.objects.create_user(**validated_data)
        logging.info("CREATE: User is created")
        return user

    class Meta(object):
        model : User = User
        fields : Tuple[str, str, str] = ('id', 'username', 'password')
        extra_kwargs : dict[str, dict[str, bool]] = {
            'password': {'write_only': True}
        }


class CategorySerializer(ModelSerializer):
    class Meta(object):
        model = Category
        fields : str = '__all__'


class GroupSerializer(ModelSerializer):
    members : UserSerializer = UserSerializer(many=True, required=False)

    class Meta(object):
        model : Groups = Groups
        fields : str = '__all__'


class UserExpenseSerializer(ModelSerializer):
    class Meta(object):
        model : UserExpense = UserExpense
        fields : List[str]= ['user', 'amount_owed', 'amount_lent']


class ExpensesSerializer(ModelSerializer):
    users : UserExpenseSerializer= UserExpenseSerializer(many=True, required=True)

    def create(self, validated_data):
        """
        Creates an Expense
        """
        expense_users = validated_data.pop('users')
        expense = Expenses.objects.create(**validated_data)
        logging.info("CREATE: expense is created")
        for eu in expense_users:
            UserExpense.objects.create(expense=expense, **eu)
        return expense

    def update(self, instance, validated_data):
        """
        Updates and saves expense
        """
        user_expenses = validated_data.pop('users')
        instance.description = validated_data['description']
        instance.category = validated_data['category']
        instance.group = validated_data.get('group', None)
        instance.total_amount = validated_data['total_amount']

        if user_expenses:
            instance.users.all().delete()
            UserExpense.objects.bulk_create(
                [
                    user_expense(expense=instance, **user_expense)
                    for user_expense in user_expenses
                ],
            )
        instance.save()
        logging.info("Update: Expense is updated and saved to db")
        return instance

    def validate(self, attrs):
        """
        Validates user. Throws an errow if single user appears multiple times
        """
        # user = self.context['request'].user
        user_ids = [user['user'].id for user in attrs['users']]
        if len(set(user_ids)) != len(user_ids):
            logging.error('Single user appears multiple times')
            raise ValidationError('Single user appears multiple times')


        return attrs

    class Meta(object):
        model = Expenses
        fields : str = '__all__'
