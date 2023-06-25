from rest_framework import serializers
from .models import Student

#validator
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name must be start with r')
    return value

class StudentSerializer(serializers.Serializer):
    name =serializers.CharField( max_length=50 , validaors = [start_with_r] )
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    # Field level validation

    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError("Seat is full")
        return value

    # Object Level validation

    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rohit' and ct.lower() != 'rachi':
            raise serializers.ValidationError('city must be rachi')
        return data