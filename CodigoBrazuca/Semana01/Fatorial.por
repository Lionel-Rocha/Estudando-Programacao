programa {
  funcao inicio() {
    
    inteiro numero, fatorial = 1

    escreva("Digite um número positivo e inteiro: ")
    leia (numero)

    para (inteiro i = 1; i <= numero; i++){
      fatorial = fatorial * i
    }

    escreva ("O fatorial de ", numero, " é ", fatorial)

  }
}