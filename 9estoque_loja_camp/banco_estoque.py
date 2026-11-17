
import sqlite3


def conectar(arquivo="estoque.db"):
    conn = sqlite3.connect(arquivo)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL,
            quantidade INTEGER,
            minimo INTEGER
        )
    """)

    conn.commit()

    return conn


def cadastrar(conn, nome, categoria, preco, quantidade=0, minimo=5):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade, minimo)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, preco, quantidade, minimo))

    conn.commit()

    return cursor.lastrowid


def listar(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM produtos
        ORDER BY nome
    """)

    return cursor.fetchall()


def buscar(conn, texto):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE nome LIKE ?
        ORDER BY nome
    """, ("%" + texto + "%",))

    return cursor.fetchall()


def entrada(conn, id, quantidade):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id = ?
    """, (quantidade, id))

    conn.commit()

    return cursor.rowcount > 0


def saida(conn, id, quantidade):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, quantidade
        FROM produtos
        WHERE id = ?
    """, (id,))

    produto = cursor.fetchone()

    if produto is None:
        return "Produto não encontrado."

    nome = produto[0]
    estoque = produto[1]

    if quantidade > estoque:
        return f"Estoque insuficiente: há {estoque} unidade(s) de {nome}."

    if quantidade <= 0:
        return "Quantidade inválida."

    cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade - ?
        WHERE id = ?
    """, (quantidade, id))

    conn.commit()

    return f"Saída registrada: {quantidade} x {nome}."


def estoque_baixo(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM produtos
        WHERE quantidade < minimo
        ORDER BY nome
    """)

    return cursor.fetchall()


def valor_total(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(preco * quantidade)
        FROM produtos
    """)

    resultado = cursor.fetchone()[0]

    if resultado is None:
        return 0

    return resultado
