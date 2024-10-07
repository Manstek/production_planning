from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Constraint(models.Model):
    problem = models.ForeignKey(Problem, related_name='constraints', on_delete=models.CASCADE)
    variable = models.CharField(max_length=50)  # Например, x1, x2, y1 и т.д.
    condition = models.CharField(max_length=2, choices=[('>=', '>='),
                                                        ('<=', '<='),
                                                        ('=', '=')])
    value = models.FloatField()

    def __str__(self):
        return f"{self.variable} {self.condition} {self.value}"
