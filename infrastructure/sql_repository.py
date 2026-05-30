import sqlite3
from core.interfaces import IAuditRepository


class SqliteAuditRepository(IAuditRepository):
    def __int__(self, db_path: str = "neuro_audit_logs.db"):
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """
        JOÃO: Aqui você escreve o SQL puro para criar as tabelas e as Triggers.
        O Python vai executar isso automaticamente quando o app abrir.
        """
        query_criacao_tabelas = """
            -- Escreva aqui o CREATE TABLE dos devs e dos laudos
            -- Escreva aqui sua CREATE TRIGGER para calcular a sanidade
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript(query_criacao_tabelas)

    def save_audit_log(
        self, author_name: str, sanity_score: int, diagnostic: str
    ) -> None:
        """
        JOÃO: Aqui você escreve o comando INSERT. A Trigger fará o resto.
        """
        query_insert = "INSERT INTO..."  # Preencha aqui

        with sqlite3.connect(self.db_path) as conn:
            conn.execute(query_insert, (author_name, sanity_score, diagnostic))
            conn.commit()

    def get_history_by_author(self, author_name: str) -> list:
        # Lógica de SELECT virá aqui
        pass
