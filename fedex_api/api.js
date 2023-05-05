const API_URL = "http://localhost:5000"; // Replace with your Flask API URL

export async function getFedexInfo(cards, jp_zipcode, us_zipcode) {
  const response = await fetch(`${API_URL}/fedex`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ cards, jp_zipcode, us_zipcode }),
  });

  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }

  return await response.json();
}