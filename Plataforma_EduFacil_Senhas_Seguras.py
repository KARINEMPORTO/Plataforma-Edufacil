
import re

def verificar_senha_segura(senha):
    criterios = {
        "Comprimento mínimo de 8 caracteres": len(senha) >= 8,
        "Letra maiúscula": bool(re.search(r'[A-Z]', senha)),
        "Letra minúscula": bool(re.search(r'[a-z]', senha)),
        "Número": bool(re.search(r'[0-9]', senha)),
        "Símbolo especial (!@#$% etc.)": bool(re.search(r'[\W_]', senha))
    }
    return criterios

def plataforma_senha_segura():
    print("=== Bem-vindo à Plataforma EduFácil: Criando Senhas Seguras ===")
    print("Sua senha precisa atender os seguintes critérios de segurança:")

    while True:
        senha = input("\nDigite uma senha para testar: ")

        criterios = verificar_senha_segura(senha)

        if all(criterios.values()):
            print("✅ Parabéns! Sua senha é segura.")
            break
        else:
            print("\n⚠️ Sua senha ainda não é segura. Veja o que está faltando:")
            for criterio, valido in criterios.items():
                if not valido:
                    print(f"- {criterio}")
            print("\nTente novamente seguindo as dicas acima.")

if __name__ == '__main__':
    plataforma_senha_segura()
