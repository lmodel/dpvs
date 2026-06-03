---
search:
  boost: 10.0
---

# Class: ProfessionalExperience 


_Information about professional experiences_



<div data-search-exclude markdown="1">



URI: [pd:ProfessionalExperience](https://w3id.org/lmodel/dpv/pd/ProfessionalExperience)





```mermaid
 classDiagram
    class ProfessionalExperience
    click ProfessionalExperience href "../ProfessionalExperience/"
      Professional <|-- ProfessionalExperience
        click Professional href "../Professional/"
      

      ProfessionalExperience <|-- WorkExperience
        click WorkExperience href "../WorkExperience/"
      

      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **ProfessionalExperience**
            * [WorkExperience](WorkExperience.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ProfessionalExperience](https://w3id.org/lmodel/dpv/pd/ProfessionalExperience) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Professional Experience




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ProfessionalExperience |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ProfessionalExperience |
| native | pd:ProfessionalExperience |
| exact | dpv_pd:ProfessionalExperience, dpv_pd_owl:ProfessionalExperience |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProfessionalExperience
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalExperience
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional experiences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Experience
exact_mappings:
- dpv_pd:ProfessionalExperience
- dpv_pd_owl:ProfessionalExperience
is_a: Professional
class_uri: pd:ProfessionalExperience

```
</details>

### Induced

<details>
```yaml
name: ProfessionalExperience
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalExperience
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional experiences
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Experience
exact_mappings:
- dpv_pd:ProfessionalExperience
- dpv_pd_owl:ProfessionalExperience
is_a: Professional
class_uri: pd:ProfessionalExperience

```
</details></div>