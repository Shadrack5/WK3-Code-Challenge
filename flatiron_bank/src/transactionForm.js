import React, { useState } from 'react';

const TransactionForm = ({ onAddTransaction }) => {
  const [transactionData, setTransactionData] = useState({
    date: '',
    description: '',
    category: '',
    amount: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setTransactionData({ ...transactionData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Perform any validation if needed
    onAddTransaction(transactionData);
    setTransactionData({
      date: '',
      description: '',
      category: '',
      amount: '',
    });
  };

  return (
    <div className="transaction-container">
      <h2> New Transactions?</h2>
      <form onSubmit={handleSubmit}>
        <div className="area">
          <input
            type="text"
            name="date"
            value={transactionData.date}
            placeholder="Date"
            onChange={handleChange}
          />
        </div>
        <div className="area">
          <input
            type="text"
            name="description"
            value={transactionData.description}
            placeholder="Description"
            onChange={handleChange}
          />
        </div>
        <div className="area">
          <input
            type="text"
            name="category"
            value={transactionData.category}
            placeholder="Category"
            onChange={handleChange}
          />
        </div>
        <div className="area">
          <input
            type="text"
            name="amount"
            value={transactionData.amount}
            placeholder="Amount"
            onChange={handleChange}
          />
        </div>
        <button id='add' type="submit">Add Transaction</button>
      </form>
    </div>
  );
};

export default TransactionForm;