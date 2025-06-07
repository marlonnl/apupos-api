from django.db import models

class Apupo(models.Model):
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True)
    
    class Meta:
        ordering = ["-id"] # ordem descendente

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": 10
        }