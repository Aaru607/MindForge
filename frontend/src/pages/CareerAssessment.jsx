import { useState } from "react";
import { api } from "../services/api";
export default function CareerAssessment() {
  const [skillLevel, setSkillLevel] = useState("");
  const [result, setResult] = useState([]);
  const submit = async () => {
    const response = await api.post("/careers/assess/", {
      email: "user@example.com",
      interests: ["Technology"],
      skill_level: skillLevel
    });
    setResult(response.data.recommendations);
  };
  return (
    <div>
      <h2>Career Assessment</h2>
      <select onChange={(e) => setSkillLevel(e.target.value)}>
        <option>Beginner</option>
        <option>Intermediate</option>
        <option>Advanced</option>
        <option>Expert</option>
      </select>
      <button onClick={submit}>Submit</button>
      <ul>
        {result.map((r, i) => <li key={i}>{r}</li>)}
      </ul>
    </div>
  );
}
