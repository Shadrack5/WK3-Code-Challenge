import React, { useState , useEffect} from 'react';
import TransactionTable from './components.js/TransactionTable';
import TransactionForm from './components.js/TransactionForm';
import SearchBar from './components.js/SearchBar';
import './index.css';


const App = () => {
  const [transactions, setTransactions] = useState([]);
  const [filteredTransactions, setFilteredTransactions] = useState([]);

  useEffect(() => {
    // Fetch data from the API here (replace 'API_URL' with the actual API endpoint)
    const API_URL = 'http://localhost:3000/transactions'; 
    fetch(API_URL)
      .then((response) => response.json())
      .then((transactions) => {
        setTransactions(transactions);
        setFilteredTransactions(transactions);
      })
      .catch((error) => console.error('Error fetching data:', error));
  }, []);

  const addTransaction = (newTransaction) => {
    setTransactions([...transactions, newTransaction]);
    setFilteredTransactions([...filteredTransactions, newTransaction]);
  };

  const deleteTransaction = (id) => {
    // Filter out the transaction with the given id and update the transactions state
    const updatedTransactions = transactions.filter((transaction) => transaction.id !== id);
    setTransactions(updatedTransactions);
  };

  const searchTransactions = (searchTerm) => {
    const filtered = transactions.filter((transaction) =>
      transaction.description.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredTransactions(filtered);
  };

  return (
    <div>
      <h1>Flatiron Bank</h1>
      <TransactionForm onAddTransaction={addTransaction} />
      <SearchBar onSearch={searchTransactions} />
      <TransactionTable transactions={transactions} onDeleteTransaction={deleteTransaction} />
    </div>
  );
};

export default App;