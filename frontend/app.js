const apiBaseUrl = "https://compass-api-eta.vercel.app";
const status = document.querySelector("#api-status");
const response = document.querySelector("#response");
const results = document.querySelector("#analysis-results");

async function checkApi() {
  try {
    const result = await fetch(`${apiBaseUrl}/api/health`);
    if (!result.ok) throw new Error("Unhealthy API");
    status.className = "status online";
    status.lastChild.textContent = " API online";
  } catch {
    status.className = "status offline";
    status.lastChild.textContent = " API offline";
  }
}

function addValue(parent, value) {
  if (Array.isArray(value)) {
    const list = document.createElement("ul");
    value.forEach((item) => {
      const entry = document.createElement("li");
      if (typeof item === "object" && item !== null) addValue(entry, item);
      else entry.textContent = item;
      list.append(entry);
    });
    parent.append(list);
  } else if (typeof value === "object" && value !== null) {
    Object.entries(value).forEach(([key, item]) => {
      const detail = document.createElement("p");
      const label = document.createElement("strong");
      label.textContent = `${key}: `;
      detail.append(label);
      if (typeof item === "object" && item !== null) addValue(detail, item);
      else detail.append(item);
      parent.append(detail);
    });
  } else {
    const paragraph = document.createElement("p");
    paragraph.textContent = value;
    parent.append(paragraph);
  }
}

function renderAnalysis(analysis) {
  results.replaceChildren();
  Object.entries(analysis).forEach(([title, value]) => {
    const section = document.createElement("article");
    const heading = document.createElement("h2");
    heading.textContent = title;
    section.append(heading);
    addValue(section, value);
    results.append(section);
  });
  results.hidden = false;
}

document.querySelector("#project-intake").addEventListener("submit", async (event) => {
  event.preventDefault();
  const button = document.querySelector("#analyze-button");
  button.disabled = true;
  button.textContent = "Analyzing...";
  response.textContent = "Compass is mapping your project.";
  results.hidden = true;

  try {
    const apiResponse = await fetch(`${apiBaseUrl}/api/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(Object.fromEntries(new FormData(event.currentTarget).entries())),
    });
    const result = await apiResponse.json();
    if (!apiResponse.ok) throw new Error(result.detail || "Analysis request failed.");
    renderAnalysis(result.analysis);
    response.textContent = result.message;
  } catch (error) {
    response.textContent = error.message || "Unable to analyze this project. Please try again.";
  } finally {
    button.disabled = false;
    button.innerHTML = 'Analyze Project <span aria-hidden="true">â†’</span>';
  }
});

checkApi();

