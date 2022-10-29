import { useState } from "react";

export default function RegistrationForm() {
  const [user, setUser] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: ""
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUser({ ...user, [e.target.name]: e.target.value });
  }

  const onSubmit = (data: any) => {
    if (user.password !== user.confirmPassword) {
      alert("Senhas não conferem");
      return;
    }
    console.log(data);
  };



  return (
    <div className="flex justify-center h-screen items-center bg-slate-100" >
      <form className="p-2 border rounded-lg h-56 shadow-md w-72 py-6 flex flex-col gap-4 bg-white" onSubmit={onSubmit}>
        <div className="flex flex-col gap-1" >
          <label htmlFor="name">Name</label>
          <input
            className="border rounded shadow-sm"
            onChange={handleChange}
            type="text"
            name="name"
            id="name"
            placeholder="Digite seu nome"
          />
        </div>
        <div className="flex flex-col gap-1" >
          <label htmlFor="email">Email</label>
          <input
            className="border rounded shadow-sm"
            onChange={handleChange}
            type="email"
            name="email"
            id="email"
            placeholder="Digite seu email"
            pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
          />
        </div>
        <div className="flex flex-col gap-1" >
          <label htmlFor="password">Password</label>
          <input
            className="border rounded shadow-sm"
            onChange={handleChange}
            type="password"
            name="password"
            id="password"
            placeholder="Digite uma senha"
          />
        </div>
        <div className="flex flex-col gap-1" >
          <label htmlFor="password">Password</label>
          <input
            className="border rounded shadow-sm"
            onChange={handleChange}
            type="password"
            name="confirmPassword"
            id="confirmPassword"
            placeholder="Digite uma senha"
          />
        </div>
        <button
          className="border rounded bg-sky-500 hover:bg-sky-700 px-2 py-1 text-white"
          type="submit" >Login</button>
      </form>
    </div>
  );
}