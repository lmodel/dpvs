---
search:
  boost: 10.0
---

# Class: ProfessionalInterview 


_Information about professional interviews_



<div data-search-exclude markdown="1">



URI: [pd:ProfessionalInterview](https://w3id.org/lmodel/dpv/pd/ProfessionalInterview)





```mermaid
 classDiagram
    class ProfessionalInterview
    click ProfessionalInterview href "../ProfessionalInterview/"
      Professional <|-- ProfessionalInterview
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **ProfessionalInterview**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ProfessionalInterview](https://w3id.org/lmodel/dpv/pd/ProfessionalInterview) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Professional Interview




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ProfessionalInterview |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ProfessionalInterview |
| native | pd:ProfessionalInterview |
| exact | dpv_pd:ProfessionalInterview, dpv_pd_owl:ProfessionalInterview |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProfessionalInterview
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalInterview
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional interviews
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Interview
exact_mappings:
- dpv_pd:ProfessionalInterview
- dpv_pd_owl:ProfessionalInterview
is_a: Professional
class_uri: pd:ProfessionalInterview

```
</details>

### Induced

<details>
```yaml
name: ProfessionalInterview
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalInterview
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional interviews
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Interview
exact_mappings:
- dpv_pd:ProfessionalInterview
- dpv_pd_owl:ProfessionalInterview
is_a: Professional
class_uri: pd:ProfessionalInterview

```
</details></div>