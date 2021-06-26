const Problem = ({ match }) => {

    const id = match.params.id

    return (
        <section id="problem">
            <div className="container py-5">
                <div className="card">
                    <div className="card-header">{id} - First Awesome Problem</div>
                    <div className="card-body">
                        <p>
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quos necessitatibus veniam dolorum dicta quasi perferendis consequatur eum harum doloremque ratione ducimus magni fugit earum tenetur deleniti, esse quaerat a ullam, molestiae iste, voluptatum culpa minus! Unde, accusantium! Illum, corrupti rem? Sequi quos rerum enim sit numquam vel dolor laudantium quibusdam. Quos necessitatibus veniam dolorum dicta quasi perferendis consequatur eum harum doloremque ratione ducimus magni fugit earum tenetur deleniti, esse quaerat a ullam, molestiae iste, voluptatum culpa minus! Unde, accusantium! Illum, corrupti rem? Sequi quos rerum enim sit numquam vel dolor laudantium quibusdam. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit rerum, deleniti quibusdam, delectus dolore obcaecati et eos temporibus quis omnis hic? Veniam, recusandae voluptates culpa illum eos quos animi beatae eum quibusdam saepe labore libero eligendi error cumque reprehenderit. Nostrum doloribus reprehenderit odit repudiandae corporis vitae excepturi porro, quo eos.
                        </p>
                    </div>
                </div>
                <div className="card">
                    <div className="card-header">Input</div>
                    <div className="card-body">
                        <p>
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                        </p>
                    </div>
                </div>
                <div className="card">
                    <div className="card-header">Output</div>
                    <div className="card-body">
                        <p>
                            Lorem ipsum dolor sit amet consectetur, adipisicing elit.
                        </p>
                    </div>
                </div>
                <div className="card">
                    <div className="card-header">Sample Input Output</div>
                    <div className="card-body">
                        <h4 className="h4 title">Sample #1</h4>
                        <div className="row px-2">
                            <div className="col-md-6 py-2">
                                <h6 className="h6">Input</h6>
                                <div className="input bg-light border-start p-3">
                                    <code>1 2 3 4</code>
                                </div>
                            </div>
                            <div className="col-md-6 py-2">
                                <h6 className="h6">Output</h6>
                                <div className="output bg-light border-start p-3">
                                    <code>Hello 10</code>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="card">
                    <div className="card-header">Submit Your Code</div>
                    <div className="card-body">
                        <form>
                            <div className="mb-3">
                                <select name="language" id="lanaguageSelect" className="form-select">
                                    <option selected>Select Language</option>
                                    <option value="c99">C</option>
                                    <option value="cpp">C++ 17</option>
                                    <option value="python">Python</option>
                                    <option value="chsarp">C#</option>
                                    <option value="java">Java</option>
                                </select>
                            </div>
                            <div className="mb-3">
                                <label for="code" class="form-label">Enter Your Code</label>
                                <textarea class="form-control" id="code" rows="12"></textarea>
                            </div>
                            <div className="mb-3">
                                <button className="btn btn-primary px-5 py-2">Submit</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Problem
