import StockViewWidget from "../components/Stockview";
import ForexViewWidget from "../components/Forexview";
import IndicesViewWidget from "../components/Indicesview";
import CryptoViewWidget from "../components/Cryptoview";
import BondsViewWidget from "../components/Bondsview";
import FutureViewWidget from "../components/Futureview";

const Dashboard = () => {
  return (
    <div className="container mx-auto mt-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div className="bg-blue-200 p-10 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-3xl font-bold mb-2">Stocks</h3>
          <StockViewWidget />
        </div>
        <div className="bg-blue-200 p-10 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-3xl font-bold mb-2">Forex</h3>
          <ForexViewWidget />
        </div>
        <div className="bg-blue-200 p-10 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-3xl font-bold mb-2">Indices</h3>
          <IndicesViewWidget />
        </div>
        <div className="bg-blue-200 p-10 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-3xl font-bold mb-2">Crypto</h3>
          <CryptoViewWidget />
        </div>
        <div className="bg-blue-200 p-10 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-3xl font-bold mb-2">Bonds</h3>
          <BondsViewWidget />
        </div>
        <div className="bg-blue-200 p-10 rounded-lg transform transition-all hover:scale-105">
          <h3 className="text-3xl font-bold mb-2">Futures</h3>
          <FutureViewWidget />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
