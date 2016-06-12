# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.urlresolvers import reverse

class AnoLetivo(models.Model):
    """Classe que representa um Ano Letivo."""

    titulo = models.CharField(max_length=15, unique=True, verbose_name=u"Ano Letivo")
    data_criacao = models.DateField(auto_now=True, verbose_name=u"Data de criação")

    def __unicode__(self):
        return u"Ano Letivo de {ano_letivo}".format(ano_letivo=self.titulo)

    class Meta:
        verbose_name = u"Ano Letivo"
        verbose_name_plural = u"Anos Letivos"


class Pessoa(models.Model):
    """Classe abstrata que representa uma Pessoa."""

    nome = models.CharField(max_length=100, verbose_name=u"Nome")
    sobrenome = models.CharField(max_length=100, verbose_name=u"Sobrenome")
    e_mail = models.EmailField(null=True)
    telefone = models.CharField(max_length=10)
    endereco = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{nome}".format(nome=self.nome)

    class Meta:
        abstract = True


class Professor(Pessoa):
    """Classe que representa um Professor."""
    usuario = models.OneToOneField(User, related_name=u"professor")

    class Meta:
        verbose_name = u"Professor"
        verbose_name_plural = u"Professores"


class Responsavel(Pessoa):
    """Classe que representa um Responsável."""
    usuario = models.OneToOneField(User, related_name=u"responsavel")

    class Meta:
        verbose_name = u"Responsável"
        verbose_name_plural = u"Responsáveis"


class Aluno(Pessoa):
    """Classe que representa um Aluno."""
    responsavel = models.ForeignKey(Responsavel, related_name=u"responsavel",
                                    verbose_name=u"Responsável")
    data_nascimento = models.DateField(null=True, verbose_name=u"Data de nascimento")
    turmas = models.ManyToManyField(u"Turma", related_name=u"alunos")

    class Meta:
        verbose_name = u"Aluno"
        verbose_name_plural = u"Alunos"


class Disciplina(models.Model):
    """Classe que representa uma Disciplina."""
    nome_disciplina = models.CharField(max_length=50)
    turma = models.ForeignKey(u"Turma", related_name=u"disciplinas")
    professor = models.ForeignKey(u"Professor", related_name=u"disciplinas")

    def __unicode__(self):
        return u"{nome_disciplina}".format(nome_disciplina=self.nome_disciplina)

    class Meta:
        verbose_name = u"Disciplina"
        verbose_name_plural = u"Disciplinas"


class Turma(models.Model):
    """Classe que representa um Turma."""
    nome_turma = models.CharField(max_length=20, verbose_name=u"Nome da Turma")
    ano_letivo = models.ForeignKey(u"AnoLetivo", related_name=u"turmas")

    def __unicode__(self):
        return u"{nome_turma}".format(nome_turma=self.nome_turma)

    class Meta:
        verbose_name = u"Turma"
        verbose_name_plural = u"Turmas"


class Notas(models.Model):
    Aluno = models.ForeignKey("Aluno")
    Disciplina = models.ForeignKey("Disciplina")
    nota1 = models.DecimalField(blank=True, verbose_name=u"Nota 1")
    nota2 = models.DecimalField(blank=True, verbose_name=u"Nota 2")
    nota3 = models.DecimalField(blank=True, verbose_name=u"Nota 3")
    nota4 = models.DecimalField(blank=True, verbose_name=u"Nota 4")
    nota5 = models.DecimalField(blank=True, verbose_name=u"Nota 5")
    nota6 = models.DecimalField(blank=True, verbose_name=u"Nota 6")
    nota7 = models.DecimalField(blank=True, verbose_name=u"Nota 7")
    nota8 = models.DecimalField(blank=True, verbose_name=u"Nota 8")