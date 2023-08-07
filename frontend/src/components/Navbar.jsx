import { Link } from "wouter";

function Navbar() {
    return (
      <nav className="bg-gray-600 p-4">
         <div className="container mx-auto flex">
            <Link href="/" className="text-white text-2xl font-bold">
                 Dashboard
            </Link>
            <div className="px-6">
                <Link href="/Stockbot" className="text-white text-2xl font-bold">
                 Stockbot
                </Link>
            </div>
            <div>
                <Link href="/team" className="text-white text-2xl font-bold">
                 Team
                </Link>
            </div>
          </div>
        </nav>
    );
}
export default Navbar;
