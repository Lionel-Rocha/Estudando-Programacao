programa {
  inclua biblioteca Util --> util
  funcao inicio() {
    //eu fiz uma implementação diferente do sugerido para dar um tempero.
    inteiro vetor[3]

    para (inteiro i = 0; i < 3; i++){
      escreva("Digite o número ", i+1, ": ")
      leia(vetor[i])
    }

    inteiro soma = 0

    para (inteiro j = 0; j < 3; j++){
      soma = soma + vetor[j]
    }

    real media = soma / 3

    escreva("A média é ", media)
    
  }
}
