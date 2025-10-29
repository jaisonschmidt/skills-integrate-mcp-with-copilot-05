"""
Módulo de Gestão de Alunos

Permite cadastrar, editar, excluir e listar alunos.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Dict

router = APIRouter()

# Banco de dados em memória para alunos
alunos_db: Dict[int, Dict] = {}
next_id = 1

@router.get("/alunos")
def listar_alunos():
    """Lista todos os alunos cadastrados"""
    return list(alunos_db.values())

@router.post("/alunos")
def cadastrar_aluno(nome: str, nascimento: str, responsavel: str = None, turma: str = None):
    """Cadastra um novo aluno"""
    global next_id
    aluno = {
        "id": next_id,
        "nome": nome,
        "nascimento": nascimento,
        "responsavel": responsavel,
        "turma": turma
    }
    alunos_db[next_id] = aluno
    next_id += 1
    return aluno

@router.put("/alunos/{aluno_id}")
def editar_aluno(aluno_id: int, nome: str = None, nascimento: str = None, responsavel: str = None, turma: str = None):
    """Edita os dados de um aluno"""
    if aluno_id not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    aluno = alunos_db[aluno_id]
    if nome:
        aluno["nome"] = nome
    if nascimento:
        aluno["nascimento"] = nascimento
    if responsavel:
        aluno["responsavel"] = responsavel
    if turma:
        aluno["turma"] = turma
    return aluno

@router.delete("/alunos/{aluno_id}")
def excluir_aluno(aluno_id: int):
    """Exclui um aluno do sistema"""
    if aluno_id not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    del alunos_db[aluno_id]
    return {"message": "Aluno excluído com sucesso"}
