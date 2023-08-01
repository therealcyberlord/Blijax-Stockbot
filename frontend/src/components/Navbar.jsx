import { Link } from "wouter";

function Navbar() {
    return (
      <nav className="bg-gray-600 p-4">
         <div className="container mx-auto flex">
            <Link href="/" className="text-white text-2xl font-bold">
                 Dashboard
            </Link>
            <div className="px-6">
                <Link href="/about" className="text-white text-2xl font-bold">
                 About
                </Link>
            </div>
          </div>
        </nav>
    );
}
export default Navbar;
