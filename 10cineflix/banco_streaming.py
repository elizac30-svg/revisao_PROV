import sqlite3
import json
from datetime import datetime


def conectar():
    conn = sqlite3.connect("cineflix.db")
    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS titulos (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            tipo TEXT,
            genero TEXT,
            ano INTEGER,
            duracao_min INTEGER,
            classificacao TEXT,
            nota REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS visualizacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            perfil TEXT,
            titulo_id INTEGER,
            minutos INTEGER,
            data TEXT,
            FOREIGN KEY (titulo_id) REFERENCES titulos(id)
        )
    """)

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM titulos")
    quantidade = cursor.fetchone()[0]

    if quantidade == 0:
        with open("catalogo.json", "r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

        for item in catalogo:
            cursor.execute("""
                INSERT INTO titulos
                (id, titulo, tipo, genero, ano, duracao_min,
                 classificacao, nota)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item["id"],
                item["titulo"],
                item["tipo"],
                item["genero"],
                item["ano"],
                item.get("duracao_min", item.get("duracao", 0)),
                item["classificacao"],
                item["nota"]
            ))

        conn.commit()
        print(f"{len(catalogo)} títulos importados do catalogo.json.")

    return conn


def listar_catalogo(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titulos ORDER BY id")
    return cursor.fetchall()


def registrar_visualizacao(conn, perfil, titulo_id, minutos):
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO visualizacoes
            (perfil, titulo_id, minutos, data)
            VALUES (?, ?, ?, ?)
        """, (
            perfil,
            titulo_id,
            minutos,
            datetime.now().strftime("%d/%m/%Y %H:%M")
        ))

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False


def historico(conn, perfil):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT visualizacoes.data, titulos.titulo, visualizacoes.minutos
        FROM visualizacoes
        JOIN titulos ON titulos.id = visualizacoes.titulo_id
        WHERE visualizacoes.perfil = ?
        ORDER BY visualizacoes.id DESC
    """, (perfil,))

    return cursor.fetchall()


def total_historico(conn, perfil):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(minutos)
        FROM visualizacoes
        WHERE perfil = ?
    """, (perfil,))

    resultado = cursor.fetchone()[0]
    return resultado if resultado is not None else 0


def mais_assistidos(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT titulos.titulo, COUNT(visualizacoes.id) AS total
        FROM visualizacoes
        JOIN titulos ON titulos.id = visualizacoes.titulo_id
        GROUP BY titulos.id
        ORDER BY total DESC
        LIMIT 5
    """)

    return cursor.fetchall()


def tempo_por_perfil(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT perfil, SUM(minutos) AS total
        FROM visualizacoes
        GROUP BY perfil
        ORDER BY total DESC
    """)

    return cursor.fetchall()


def exportar_relatorio(conn):
    relatorio = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "mais_assistidos": [],
        "tempo_por_perfil": []
    }

    for titulo, total in mais_assistidos(conn):
        relatorio["mais_assistidos"].append({
            "titulo": titulo,
            "visualizacoes": total
        })

    for perfil, minutos in tempo_por_perfil(conn):
        relatorio["tempo_por_perfil"].append({
            "perfil": perfil,
            "minutos": minutos
        })

    with open("relatorio.json", "w", encoding="utf-8") as arquivo:
        json.dump(relatorio, arquivo, ensure_ascii=False, indent=4)

    return "Relatório exportado para relatorio.json!"
