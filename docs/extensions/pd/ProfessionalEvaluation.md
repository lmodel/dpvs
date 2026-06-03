---
search:
  boost: 10.0
---

# Class: ProfessionalEvaluation 


_Information about professional evaluations_



<div data-search-exclude markdown="1">



URI: [pd:ProfessionalEvaluation](https://w3id.org/lmodel/dpv/pd/ProfessionalEvaluation)





```mermaid
 classDiagram
    class ProfessionalEvaluation
    click ProfessionalEvaluation href "../ProfessionalEvaluation/"
      Professional <|-- ProfessionalEvaluation
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **ProfessionalEvaluation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ProfessionalEvaluation](https://w3id.org/lmodel/dpv/pd/ProfessionalEvaluation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Professional Evaluation




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ProfessionalEvaluation |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ProfessionalEvaluation |
| native | pd:ProfessionalEvaluation |
| exact | dpv_pd:ProfessionalEvaluation, dpv_pd_owl:ProfessionalEvaluation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProfessionalEvaluation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalEvaluation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional evaluations
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Evaluation
exact_mappings:
- dpv_pd:ProfessionalEvaluation
- dpv_pd_owl:ProfessionalEvaluation
is_a: Professional
class_uri: pd:ProfessionalEvaluation

```
</details>

### Induced

<details>
```yaml
name: ProfessionalEvaluation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalEvaluation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional evaluations
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Evaluation
exact_mappings:
- dpv_pd:ProfessionalEvaluation
- dpv_pd_owl:ProfessionalEvaluation
is_a: Professional
class_uri: pd:ProfessionalEvaluation

```
</details></div>