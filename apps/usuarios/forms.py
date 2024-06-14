from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao_silva'
                }
            )
        )
    
    senha = forms.CharField(
        label="Senha:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
                }
            )
        )
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao_silva'
                }
            )
        )
    
    email = forms.EmailField(
        label="E-mail:",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@email.com'
                }
            )
        )
    
    senha_1 = forms.CharField(
        label="Senha:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha'
                }
            )
        )
    
    senha_2 = forms.CharField(
        label="Confirme a senha:",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha novamente'
                }
            )
        )
    
    def clean_nome_cadastro(self): #nome dessa funçao deve ser 'clean_(campo a ser validado)' para o django fazer o processo correto
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('Não são permitidos espaços nesse campo')
            else:
                return nome
            

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas informadas não são iguais')
        else:
            return senha_2
