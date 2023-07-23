import React from 'react';

const TransactionTable = ({ transactions, onDeleteTransaction }) => {
  return (
    <div className='completedtransactions'> 
      <h2 className='completedtransactions'>Completed Transactions</h2>
      <ul className=''>
        {transactions.map((transaction) => (
          <li key={transaction.id}>
            <div>
              <strong>Date:</strong> {transaction.date}
            </div>
            <div>
              <strong>Description:</strong> {transaction.description}
            </div>
            <div>
              <strong>Category:</strong> {transaction.category}
            </div>
            <div>
              <strong>Amount:</strong> {transaction.amount}
            </div>
            <button onClick={() => onDeleteTransaction(transaction.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TransactionTable;