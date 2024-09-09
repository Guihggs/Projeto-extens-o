import psycopg2
from datetime import datetime

class AgendaPet:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="agenda_pet",
            user="guilherme",
            password="123456",
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS passeios (
            id SERIAL PRIMARY KEY,
            morador VARCHAR(100),
            pet VARCHAR(100),
            horario TIMESTAMP
        )
        """)
        self.conn.commit()

    def agendar_passeio(self, morador, pet, horario):
        self.cursor.execute("""
        INSERT INTO passeios (morador, pet, horario)
        VALUES (%s, %s, %s)
        """, (morador, pet, horario))
        self.conn.commit()
        print(f"Passeio agendado para {pet} de {morador} às {horario}")

    def visualizar_agenda(self):
        self.cursor.execute("SELECT morador, pet, horario FROM passeios")
        passeios = self.cursor.fetchall()
        for morador, pet, horario in passeios:
            print(f"Horário: {horario} - {pet} de {morador}")

    def close(self):
        self.cursor.close()
        self.conn.close()

# Exemplo de uso
agenda = AgendaPet()
agenda.agendar_passeio("João", "Rex", datetime(2024, 9, 10, 8, 0))
agenda.agendar_passeio("Maria", "Luna", datetime(2024, 9, 10, 9, 0))
agenda.visualizar_agenda()
agenda.close()
