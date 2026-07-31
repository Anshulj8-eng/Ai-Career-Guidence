let detectedSkills = [];
let fullResumeText = "";
let skillChart;
let missingChart;
let jobChart;
let resultBox =
document.getElementById("resultBox");


/* Upload Resume */


document.getElementById("uploadBtn")
.addEventListener("click",()=>{

document.getElementById("resumeFile")
.click();

});



document.getElementById("resumeFile")
.addEventListener("change",async ()=>{

let file =
document.getElementById("resumeFile")
.files[0];

let formData = new FormData();

formData.append(
"resume",
file
);

let response =
await fetch(
"http://127.0.0.1:5000/upload_resume",
{
method:"POST",
body:formData
}
);

let data =
await response.json();

detectedSkills =
data.skills;

fullResumeText =
data.resume_text;

document.getElementById("totalSkills").innerText =
data.skills.length;

resultBox.innerHTML=
`
<h2>Resume Analysis</h2>

<b>Detected Skills:</b><br>

${data.skills.join("<br>")}

`;

});
/* Skill Gap */

document.getElementById("skillBtn")
.addEventListener(
"click",
async ()=>{

let role =
document.getElementById(
"targetRole"
).value;

try{

let response=
await fetch(
"http://127.0.0.1:5000/skill_gap",
{

method:"POST",

headers:{
"Content-Type":
"application/json"
},

body:JSON.stringify({

role:role,
skills:detectedSkills

})

}

);

let data=
await response.json();
drawSkillChart(
data.match_score
);

drawMissingChart(
data.missing_skills
);
document.getElementById(
"matchPercent"
).innerText=
data.match_score + "%";

document.getElementById(
"missingCount"
).innerText=
data.missing_skills.length;


resultBox.innerHTML=
`
<h2>Skill Analysis</h2>

<b>Target Role:</b>
${data.role}

<br><br>

<b>Detected Skills:</b>
<br>

${data.detected_skills.join("<br>")}

<br><br>

<b>Missing Skills:</b>
<br>

${data.missing_skills.join("<br>")}

<br><br>

<b>Skill Match:</b>
${data.match_score}%

`;

}

catch(error){

console.log(error);

alert("Skill Gap Error");

}

});


/* Job Recommendation */

document.getElementById("jobBtn")
.addEventListener("click", async ()=>{

try{

let response = await fetch(
"http://127.0.0.1:5000/recommend_jobs",
{
method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

skills:detectedSkills

})

}
);

let data = await response.json();
document.getElementById("jobCount").innerText =
data.recommended_jobs?.length || 0;
drawJobChart(
data.recommended_jobs
);

document.getElementById(
"jobCount"
).innerText =
data.recommended_jobs.length;


resultBox.innerHTML=`

<h2>Recommended Jobs</h2>

${data.recommended_jobs.join("<br><br>")}

`;

}

catch(error){

console.log(error);

alert("Job Recommendation Error");

}

});
/* Interview Questions */

document.getElementById("interviewBtn")
.addEventListener("click",()=>{

let questions=[];

if(detectedSkills.includes("python") || detectedSkills.includes("Python")){

questions.push(
"What are lists and tuples in Python?"
);

questions.push(
"What is the difference between class and object in Python?"
);

}

if(
detectedSkills.includes("machine learning") ||
detectedSkills.includes("Machine Learning")
){

questions.push(
"What is overfitting?"
);

questions.push(
"What is the difference between supervised and unsupervised learning?"
);

questions.push(
"What is feature engineering?"
);

}

if(
detectedSkills.includes("flask") ||
detectedSkills.includes("Flask")
){

questions.push(
"What is Flask?"
);

questions.push(
"What is the difference between GET and POST methods?"
);

}

if(
detectedSkills.includes("html") ||
detectedSkills.includes("HTML")
){

questions.push(
"What is semantic HTML?"
);

}

if(
detectedSkills.includes("css") ||
detectedSkills.includes("CSS")
){

questions.push(
"What is the difference between Flexbox and Grid?"
);

}

if(
detectedSkills.includes("javascript") ||
detectedSkills.includes("JavaScript")
){

questions.push(
"What is the difference between var, let and const?"
);

}

if(
detectedSkills.includes("mysql") ||
detectedSkills.includes("SQL")
){

questions.push(
"What is a primary key?"
);

questions.push(
"What is a JOIN?"
);

}

if(questions.length===0){

questions = [

"Tell me about yourself",

"What are your strengths?",

"Why should we hire you?",

"Describe a challenging project"

];

}

resultBox.innerHTML=`

<h2>Interview Questions</h2>

${questions.map(
(q,index)=>`${index+1}. ${q}<br><br>`
).join("")}

`;

});

/* Chatbot */

let chatIcon=
document.getElementById("chatIcon");

let chatbot=
document.getElementById("chatbot");

let closeChat=
document.getElementById("closeChat");

chatIcon.addEventListener("click",()=>{

chatbot.style.display="flex";

});

closeChat.addEventListener("click",()=>{

chatbot.style.display="none";

});


document.getElementById("sendBtn")
.addEventListener("click",async()=>{

let message=
document.getElementById("message").value;

if(message=="") return;

let body=
document.getElementById("chatBody");

body.innerHTML +=
`<div class='user'>${message}</div>`;

let response=await fetch(
"http://127.0.0.1:5000/chat",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
message:message
})
}
);

let data=
await response.json();
document.getElementById(
"jobCount"
).innerText=
data.recommended_jobs.length;

body.innerHTML +=
`<div class='bot'>${data.response}</div>`;

document.getElementById(
"message"
).value="";

body.scrollTop=
body.scrollHeight;

});
function scrollToSection(id){

document
.getElementById(id)
.scrollIntoView({

behavior:"smooth"

});

}

function openChat(){

document
.getElementById("chatbot")
.style.display="flex";

}

function showProfile(){

window.location.href=
"http://127.0.0.1:5000/download_resume";

}
function drawSkillChart(match){

if(skillChart){
skillChart.destroy();
}

let ctx=
document
.getElementById(
"skillChart"
);

skillChart=
new Chart(ctx,{

type:"pie",

data:{

labels:[
"Matched",
"Remaining"
],

datasets:[{

data:[
match,
100-match
]

}]

}

});

}



function drawMissingChart(skills){

if(missingChart){
missingChart.destroy();
}

let ctx=
document
.getElementById(
"missingChart"
);

missingChart=
new Chart(ctx,{

type:"bar",

data:{

labels:skills,

datasets:[{

label:"Missing Skills",

data:
skills.map(()=>1)

}]

}

});

}



function drawJobChart(jobs){

if(jobChart){
jobChart.destroy();
}

let ctx=
document
.getElementById(
"jobChart"
);

jobChart=
new Chart(ctx,{

type:"doughnut",

data:{

labels:jobs,

datasets:[{

label:
"Job Suitability",

data:
jobs.map(
()=>20
)

}]

}

});

}