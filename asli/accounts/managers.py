from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def cretae_user(self,phone,email,password):
        if not phone:
            raise ValueError('Errore Phone')
        if not email:
            raise ValueError('Errore Email')
        
        user=self.model(phone=phone,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,phone,email,password):
        user=self.cretae_user(phone,email,password)
        user.is_admin=True
        user.save(using=self._db)
        return user
         