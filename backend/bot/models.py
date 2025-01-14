from django.db import models

class User(models.Model):
    line_id = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=255, null=True, blank=True)
    pic_url = models.URLField(null=True, blank=True)
    age_group = models.CharField(max_length=10, choices=[('青世代', '青世代'), ('銀世代', '銀世代')])
    status = models.CharField(max_length=20, default='idle') # idle, questioning, answering, writing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.display_name}"

class AudioMessage(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message_id = models.CharField(max_length=50)
    file_path = models.CharField(max_length=255, null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Audio from {self.user} at {self.created_at}"

class Conversation(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    message = models.TextField()
    is_from_user = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{'User' if self.is_from_user else 'Bot'}: {self.message[:50]}"

class Question(models.Model):
    asker = models.ForeignKey('User', on_delete=models.CASCADE)
    asker_group = models.CharField(max_length=10, choices=[('青世代', '青世代'), ('銀世代', '銀世代')])
    content = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('傳統技藝', '傳統技藝'),
        ('歷史文化', '歷史文化'),
        ('佳餚食譜', '佳餚食譜'),
        ('科技新知', '科技新知'),
        ('人生經驗', '人生經驗'),
        ('其他', '其他'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='waiting') # waiting, answered
    response_counter = models.IntegerField(default=0)

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    responder = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    description = models.TextField()
    content = models.TextField()
    cover = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=50, choices=[
        ('傳統技藝', '傳統技藝'),
        ('歷史文化', '歷史文化'),
        ('佳餚食譜', '佳餚食譜'),
        ('科技新知', '科技新知'),
        ('人生經驗', '人生經驗'),
        ('其他', '其他'),
    ])
    tags = models.JSONField(default=list)
    input_text = models.TextField(default="")
    likes = models.IntegerField(default=0)
    liked_by = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    number = models.IntegerField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.number} of {self.article.title}"