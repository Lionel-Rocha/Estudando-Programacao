programa {
  funcao inicio() {
    
    inteiro ano

    escreva("Digite um ano para saber se ele é bissexto ou não: ")
      leia(ano)

    se((ano % 4 == 0) e (ano % 100 != 0) ou (ano % 400 == 0)){
      escreva("O ano é bissexto")
    }senao{
      escreva("O ano não é bissexto")
    }

  }
}