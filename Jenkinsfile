pipeline {
    agent any
    stages {
        // stage('Build and Test - Scenario 1 (Success)') {
        //     steps {
        //         script {
        //             echo 'Iniciando o build e teste no container Docker...'

        //             docker.build('gcjenkins-build', '-f Dockerfile.build .').inside {
        //                 echo 'Dependências instaladas e ambiente de build preparado.'
        //             }
        //             docker.build('gcjenkins-test', '-f Dockerfile.test .').inside {
                        
        //                 sh """PYTHONPATH=. pytest tests/""" 
        //                 echo 'Testes executados com sucesso no container Docker.'
        //             }
        //         }
        //     }
        //     post {
        //         success {
        //             echo 'Cenário 1: Build e Testes OK!'
        //         }
        //     }
        // }
        // stage('Build - Scenario 2 (Build Failure)') {
        //     steps {
        //         script {
        //             echo 'Tentando build para Cenário 2 (simulando falha de compilação/linting)...'
        //             try {
        //                 docker.build('gcjenkins-build', '-f Dockerfile.build .').inside {
        //                     sh """python -c "import sys; print('Simulando erro de sintaxe ou de build'); sys.exit(1)" """
        //                 }
        //                 error('O build deveria ter falhado para o Cenário 2, mas passou. Verifique o código fonte ou o comando de simulação.')
        //             } catch (Exception e) {
        //                 echo "Cenário 2: Build falhou como esperado: ${e.getMessage()}"
        //                 throw e
        //             }
        //         }
        //     }
        //     post {
        //         failure {
        //             echo 'Cenário 2: Build falhou como esperado!'
        //         }
        //         success {
        //             echo 'Cenário 2: Erro! O build não deveria ter tido sucesso.'
        //         }
        //     }
        // }

        stage('Build and Test - Scenario 3 (Unstable - Test Failure)') {
            steps {
                script {
                    echo 'Iniciando build e teste para Cenário 3 (simulando falha de teste)...'
                    docker.build('gcjenkins-build', '-f Dockerfile.build .').inside {
                        echo 'Dependências instaladas e ambiente de build preparado para Cenário 3.'
                    }

                    try {
                        docker.build('gcjenkins-test', '-f Dockerfile.test .').inside {
                            sh """PYTHONPATH=. pytest tests/""" 
                        }
                        error('Os testes deveriam ter falhado para o Cenário 3, mas passaram. Verifique o código fonte.')
                    } catch (Exception e) {
                        echo "Cenário 3: Testes falharam como esperado: ${e.getMessage()}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                unstable {
                    echo 'Cenário 3: Build instável (testes falharam) como esperado!'
                }
                success {
                    echo 'Cenário 3: Erro! Os testes não deveriam ter tido sucesso.'
                }
            }
        }
    }

    triggers {
        cron '* * * * *' 
    }
    post {
        always {
            echo 'Pipeline concluído.'
        }
        success {
            echo 'Parabéns! O pipeline foi bem-sucedido.'
        }
        failure {
            echo 'O pipeline falhou. Verifique os logs para mais detalhes.'
        }
        unstable {
            echo 'O pipeline foi instável (testes falharam).'
        }
    }
}