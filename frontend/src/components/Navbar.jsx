import { Link } from "wouter";

function Navbar() {
  return (
    <nav className="h-14 bg-gradient-to-r from-sky-500 to-indigo-500">
      <div className="container mx-auto flex">
        <Link href="/" className="text-blue text-4xl font-bold">
          Dashboard
        </Link>
        <div className="px-6">
          <Link href="/Stockbot" className="text-blue text-4xl font-bold">
            Stockbot
          </Link>
        </div>
        <div>
          <Link href="/team" className="text-blue text-4xl font-bold">
            Team
          </Link>
        </div>
        <div className="px-6">
          <Link href="/About" className="text-blue text-4xl font-bold">
            About
          </Link>
        </div>
      </div>
    </nav>
  );
}
export default Navbar;
