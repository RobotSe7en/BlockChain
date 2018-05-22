# -*- coding: UTF-8 -*-
# author by: D.W.
# created: 2018.05.14
# 区块链学习


import time, hashlib

# 创建区块链类
class Blockchain(object):
	"""
	区块链是一个连续增长的记录链表，每一个记录成为区块(block)，块与块之间用密码学技术相互连接(Hash等)。
	每一个块主要记录着前一个块的hash值、时间戳和交易数据。区块链的设计就决定了它是不可更改的。
	经典的区块链种类分为公有链(完全开放)、私有链(不开放)和联盟链(不同团体相互开放)。
	block示例：
	block = {
		'index': 1,
		'timestamp': 1506057125.900785,
		'transaction': [
			{
			'sender': '8527147fe1f5426f9dd545de4b27ee00',
			'recipient': 'a77f5cdfa2934df3954a5c7c7da5df1f',
			'amount': 5
			}
		],
		'proof': 324984774000,
		'previous_hash': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

	}
	"""
	def __init__(self):
		self.chain = []
		self.transaction = []

		# 创建创始区块
		self.new_block(previous_hash=1, proof=100)

	def new_transaction(sefl, sender, recipient, amount):
		'''
		将新交易添加到区块链
		sender: 交易发送人标识
		recipient: 交易接受人标识
		amount: 交易量
		'''
		self.transaction.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount
			})
		
		return self.last_block['index'] + 1

	def new_block(sefl, proof, previous_hash=None):
		'''
		创建新的区块并添加到区块链
		'''
		block = {
			'index': len(self.chain)+1,
			'timestamp': time.time(),
			'transaction': self.transaction,
			'proof': proof,
			'previous_hash': previous_hash or self.hash()
		}
		# 重置当前交易
		self.transaction = []

		# 将新块添加到区块链中
		self.chain.append(block)

		return block

	@staticmethod
	def hash(sefl):
		# 加密一个区块
		pass

	@property
	def last_block(self):
		# 返回区块链的最后一个区块
		pass
	



		