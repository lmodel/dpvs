---
search:
  boost: 10.0
---

# Class: ProfessionalTraining 


_Information about professional training_



<div data-search-exclude markdown="1">



URI: [pd:ProfessionalTraining](https://w3id.org/lmodel/dpv/pd/ProfessionalTraining)





```mermaid
 classDiagram
    class ProfessionalTraining
    click ProfessionalTraining href "../ProfessionalTraining/"
      Professional <|-- ProfessionalTraining
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **ProfessionalTraining**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ProfessionalTraining](https://w3id.org/lmodel/dpv/pd/ProfessionalTraining) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Professional Training




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ProfessionalTraining |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ProfessionalTraining |
| native | pd:ProfessionalTraining |
| exact | dpv_pd:ProfessionalTraining, dpv_pd_owl:ProfessionalTraining |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProfessionalTraining
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalTraining
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional training
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Training
exact_mappings:
- dpv_pd:ProfessionalTraining
- dpv_pd_owl:ProfessionalTraining
is_a: Professional
class_uri: pd:ProfessionalTraining

```
</details>

### Induced

<details>
```yaml
name: ProfessionalTraining
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalTraining
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional training
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Training
exact_mappings:
- dpv_pd:ProfessionalTraining
- dpv_pd_owl:ProfessionalTraining
is_a: Professional
class_uri: pd:ProfessionalTraining

```
</details></div>