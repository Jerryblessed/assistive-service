import { Client, xrpToDrops, dropsToXrp } from "xrpl";
import React, { useEffect, useState } from "react";
import "./App.css"; // Import your custom CSS for styling

function App() {
  const [balance, setBalance] = useState(0);
  const [wallet, setWallet] = useState("");
  const [client] = useState(new Client("wss://s.altnet.rippletest.net:51233"));
  const [paymentButtonText, setPaymentButtonText] = useState(
    "Wait for the wallet to be funded..."
  );
  const [statusText, setStatusText] = useState("");
  const [paymentInProgress, setPaymentInProgress] = useState(false);
  const [paymentAmount, setPaymentAmount] = useState("22"); // Default payment amount

  useEffect(() => {
    client.connect().then(() => {
      client.fundWallet().then((fundResult) => {
        setBalance(fundResult.balance);
        setWallet(fundResult.wallet);
        setPaymentButtonText(`Send ${paymentAmount} XRP Payment!`);
      });
    });
  }, [paymentAmount]);

  async function sendPayment() {
    setStatusText(`Sending a payment for ${paymentAmount} XRP...`);
    setPaymentInProgress(true);

    await new Promise((resolve) => setTimeout(resolve, 1000)); // Delay for 1 second

    setStatusText("Redirecting to Assitive service dashboard...");
    setTimeout(() => {
      window.location.href = "http://127.0.0.1:8000/class/";
    }, 1000); // Delay for 1 second (adjust as needed)

    const tx = {
      TransactionType: "Payment",
      Account: wallet.address,
      Amount: xrpToDrops(paymentAmount),
      Destination: "rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
    };

    try {
      const submittedTx = await client.submitAndWait(tx, {
        autofill: true,
        wallet: wallet,
      });

      setStatusText(
        `Payment Successful! Transaction Hash: ${submittedTx.hash}`
      );

      const accountInfo = await client.request({
        command: "account_info",
        account: wallet.address,
      });

      const updatedBalance = accountInfo.result.account_data.Balance;
      setBalance(dropsToXrp(updatedBalance));
    } catch (error) {
      setStatusText(`Payment Failed: ${error.message}`);
    } finally {
      setPaymentInProgress(false);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>XRP Pay</h1>
        <p>Your Wallet Balance: {balance} XRP</p>
      </header>
      <div className="payment-container">
        <div className="payment-form">
          <div className="form-group">
            <label htmlFor="paymentAmount">Payment Amount (XRP)</label>
            <input
              type="number"
              id="paymentAmount"
              placeholder="Enter Amount"
              value={paymentAmount}
              onChange={(e) => setPaymentAmount(e.target.value)}
            />
          </div>
          <button
            onClick={sendPayment}
            disabled={paymentInProgress}
            className={paymentInProgress ? "disabled" : ""}
          >
            {paymentButtonText}
          </button>
        </div>
        <p className="status-text">{statusText && <i>{statusText}</i>}</p>
      </div>
    </div>
  );
}

export default App;
