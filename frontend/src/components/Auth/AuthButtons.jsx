export default function OAuthButtons() {
    const handleTwitterAuth = () => {
      window.location.href = 'http://localhost:5000/auth/twitter';
    };
  
    return (
      <button 
        onClick={handleTwitterAuth}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg flex items-center gap-2"
      >
        <img src="/icons/twitter.svg" className="w-5 h-5" alt="Twitter logo" />
        Connect Twitter
      </button>
    );
  }