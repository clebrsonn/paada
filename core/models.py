# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


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

    class Meta:
        verbose_name = u"Aluno"
        verbose_name_plural = u"Alunos"


    def adicionar_nota(self):
        return mark_safe(u"<button class='button' href=''>Adicionar notas</button>")