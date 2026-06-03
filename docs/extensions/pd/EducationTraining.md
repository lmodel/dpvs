---
search:
  boost: 10.0
---

# Class: EducationTraining 


_Information about training as education_



<div data-search-exclude markdown="1">



URI: [pd:EducationTraining](https://w3id.org/lmodel/dpv/pd/EducationTraining)





```mermaid
 classDiagram
    class EducationTraining
    click EducationTraining href "../EducationTraining/"
      Education <|-- EducationTraining
        click Education href "../Education/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * [Education](Education.md)
            * **EducationTraining**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EducationTraining](https://w3id.org/lmodel/dpv/pd/EducationTraining) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Education Training




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EducationTraining |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EducationTraining |
| native | pd:EducationTraining |
| exact | dpv_pd:EducationTraining, dpv_pd_owl:EducationTraining |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EducationTraining
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EducationTraining
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about training as education
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education Training
exact_mappings:
- dpv_pd:EducationTraining
- dpv_pd_owl:EducationTraining
is_a: Education
class_uri: pd:EducationTraining

```
</details>

### Induced

<details>
```yaml
name: EducationTraining
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EducationTraining
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about training as education
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Education Training
exact_mappings:
- dpv_pd:EducationTraining
- dpv_pd_owl:EducationTraining
is_a: Education
class_uri: pd:EducationTraining

```
</details></div>