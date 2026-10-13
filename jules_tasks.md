# 🚀 PC_Station_5 - Plano de Execução Paralela de Agentes (Fork do AnyPS5)

Olá, Jules. Este arquivo contém a definição de escopo para execução paralela de 14 tarefas concorrentes no projeto PC_Station_5.
Por favor, processe os marcadores abaixo iniciando as tarefas simultaneamente em ramificações (branches) separadas a partir da `main`.

## 🧠 Camada de CPU e System Libraries (Agentes 1 a 4)
- [ ] **Agente 1 (CPU Linker):** Mapear as funções de sistema restantes das bibliotecas dinâmicas (.prx) do PS5 para chamadas nativas do SO Host (estilo Wine/Proton).
- [ ] **Agente 2 (ABI Translation):** Validar as convenções de chamada (ABI) e alinhamento de pilha na transição x86-64 do executável do console para o PC.
- [ ] **Agente 3 (System Stubs):** Criar stubs de simulação para as chamadas de sistema (syscalls) proprietárias da Sony que ainda não possuem mapeamento funcional.
- [ ] **Agente 4 (CPU Unit Tests):** Desenvolver testes unitários automatizados para validar a estabilidade do relinker em loops de execução de CPU.

## 🎨 Pipeline de GPU Shader (RDNA 2 para Vulkan) (Agentes 5 a 9)
- [ ] **Agente 5 (Decoder RDNA2):** Otimizar o decodificador das 1.166 instruções de shader da GPU (Oberon/RDNA2) focando em latência de tradução.
- [ ] **Agente 6 (SPIR-V Compiler):** Garantir que o recompilador converta o binário do shader em SPIR-V de forma limpa, seguindo a especificação Vulkan mais recente.
- [ ] **Agente 7 (Pipeline State):** Mapear o gerenciamento de estados de pipeline de hardware da GPU do PS5 para os equivalentes em VkPipeline.
- [ ] **Agente 8 (Texture Formats):** Implementar a conversão nativa em tempo de execução de formatos de texturas proprietários do console para formatos aceitos pelo driver Vulkan de PC.
- [ ] **Agente 9 (Shader Unit Tests):** Criar uma suite de testes que compare a saída SPIR-V gerada com os opcodes RDNA2 originais para evitar falhas visuais.

## 💾 Subsistemas de Infraestrutura e IO (Agentes 10 a 12)
- [ ] **Agente 10 (Memory Manager):** Gerenciar o mapeamento de memória unificada do console (vRAM/sysRAM compartilhadas) no espaço de endereçamento virtual do PC.
- [ ] **Agente 11 (Thread Sync):** Implementar primitivas de sincronização e agendamento de threads imitando as prioridades do kernel do PS5.
- [ ] **Agente 12 (Audio/IO Subsystem):** Estruturar os stubs de decodificação de áudio (AT9/templates) e o sistema de arquivos virtual (VFS) para leitura dos arquivos do jogo.

## 🤖 Automação e Integração Contínua (Agentes 13 e 14)
- [ ] **Agente 13 (CI Test Automation):** Configurar cenários de teste em pipelines de CI para simular a inicialização e tratamento de exceções das ramificações unificadas.
- [ ] **Agente 14 (Conflict Resolver):** Analisar preventivamente dependências cruzadas entre os agentes de CPU e GPU para planejar merges sem quebras de build.
