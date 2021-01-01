questions = [
    "My ideal economy involves a central bank which is capable of regulating the money supply through \
    inflation/deflation (defined as any increase/decrease in the money supply, regardless of demand for money), \
    reserve requirements, or fiscal policy.",
    "Value can be created through trade.",
    "All value is derived from labor.",
    "Capitalism—defined as the ownership of most capital in the hands of a bourgeois class—is an inherently unjust \
    system.",
    "Private property is one of the foundations of a good economy.",
    "It is more important to enforce existing contracts than to achieve greater equality—of either opportunity or \
    outcome—in the economy (e.g. student loans).",
    "Recessions like the Great Depression or the subprime mortgage crisis of 2007 expose the flaws of a system based \
    on free-market enterprise.",
    "If we must have a free-market economy, it should be accompanied by a high inheritance tax in order to “even the \
    playing field” each generation.",
    "A free market is better at distributing resources than a planned economy.",
    "An ideal society would have far lower taxes and far less regulations across the board.",
    "Everyone should be able to participate in running the government via elections, regardless of who you are (e.g. \
    age, criminal history).",
    "The United States should abolish their electoral college system, in favor of a direct popular vote for the \
    presidency.",
    "Representatives in the Congress cannot be adequately trusted to run the nation, and thus direct democracy is the \
    best form of government for the American people.",
    "Helping its own citizens should be a greater priority for a government than helping the citizens of other \
    countries.",
    "Undocumented immigrants should be allowed to obtain driver’s licenses, employment, social security, and other \
    benefits from the government.",
    "International organizations, such as the European Union, United Nations, and NATO, should be disbanded or \
    severely weakened.",
    "First-world countries should open their borders completely.",
    "If a set of responsibilities can be effectively delegated to a lower political entity, it should be done.",
    "Law enforcement—either public or private—is good for society.",
    "You should be able to sell your vote.",
    "I support the Sexual Revolution of the 1960s (defined as the normalization of pornography, homosexual actions, \
    contraception, and fornication).",
    "Marriage, according to my definition of marriage, should be endorsed by the government.",
    "I oppose all forms of abortion, defined as intentionally terminating the existence of an unborn child.",
    "It is ethical for one to consume any type of drugs one wants to in the privacy of one’s own home.",
    "Traditional family structures (families consisting of one working parent, one caretaker, and children) are \
    unnecessary, restrictive institutions.",
    "Polygamous relationships are inherently unethical.",
    "Hedonic pleasure is the highest moral good.",
    "If there exists a way to effectively ban pornography, it should be done.",
    "Religious values are important for a civil society.",
    "My religion (if I had one) would influence my political beliefs."
]

default_choices = [
    ("2", "Strongly agree"),
    ("1", "Somewhat agree"),
    ("-1", "Somewhat disagree"),
    ("-2", "Strongly disagree")
]

if __name__ == "__main__":
    for i in range(1, 31):
        my_string = f"""
            <div class="form-group">
                {{{{ form.question{i}.label(class="form-control-label") }}}}
                {{% if form.question{i}.errors %}}
                {{{{ form.question{i}(class="form-control form-control-lg is-invalid") }}}}
                <div class="invalid-feedback">
                    {{% for error in form.question{i}.errors %}}
                    <span>{{{{ error }}}}</span>
                    {{% endfor %}}
                </div>
                {{% else %}}
                {{% for subfield in form.question{i} %}}
                    <br>
                    {{{{ subfield }}}}
                    {{{{ subfield.label }}}}
                {{% endfor %}}
                {{% endif %}}
            </div>"""
        print(my_string)
