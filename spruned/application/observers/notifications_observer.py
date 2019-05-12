import subprocess
from spruned.application.logging_factory import Logger


class NotificationsObserver:
    def __init__(self):
        self.blocks_command = None
        self.transactions_command = None
        self.alerts_command = None

    async def on_block(self, blockheader: dict):
        if self.blocks_command:
            Logger.notifications.debug(
                'Running blocks command %s on block %s', self.blocks_command, blockheader
            )
            subprocess.run([self.blocks_command, blockheader['block_hash']])

    async def on_transaction(self, transaction_id: str):
        if self.transactions_command:
            Logger.notifications.debug(
                'Running transactions command %s on block %s', self.transactions_command, transaction_id
            )
            subprocess.run([self.transactions_command, transaction_id])

    async def on_alert(self, message: str):
        if self.alerts_command:
            Logger.notifications.debug(
                'Running alerts command %s on block %s', self.alerts_command, message
            )
            subprocess.run([self.alerts_command, message])