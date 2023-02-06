from rest_framework import serializers
from .models import Task

def start_with_c(value):
    if value[0].lower() != 'c':
        raise serializers.ValidationError('Starts with C')

def containt_numbers(value):
    if any(i.isdigit() for i in value):
        raise serializers.ValidationError('Not contain numbers')

class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[start_with_c, containt_numbers])
    class Meta:
        model = Task 
        fields = ('id', 'name', 'priority', 'created_at', 'finished_at', )

# CORS -> Cross Orgin Resource Sharing

    # def validate_name(self, value):
        
    #     condicion = True 
    #     list = [str(i) for i in range(0, 10)]
    #     while condicion:
    #         for i in value:
    #             if i in list:
    #                 condicion = False
    #         break;

    #     if condicion == False:
    #         raise serializers.ValidationError('Not numbers')
        
    #     return value

    # def validate_priority(self, value):
    #     if value is None: 
    #         return value
    #     if value < 1 or value > 3:
    #         raise serializers.ValidationError('Range 1 and 3')
    #     return value

    def validate(self, data):
        priority = data.get('priority')
        name = data.get('name')

        # if contain_number(name):
        #     raise serializers.ValidationError('Name not contain numbers')

        if priority != None and (priority < 1 or priority > 3):
            raise serializers.ValidationError('Range 1 and 3')

        return data

# def contain_number(string):
#     return any(char.isdigit() for char in string)