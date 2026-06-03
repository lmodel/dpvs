---
search:
  boost: 10.0
---

# Class: EmploymentHistory 


_Information about employment history_



<div data-search-exclude markdown="1">



URI: [pd:EmploymentHistory](https://w3id.org/lmodel/dpv/pd/EmploymentHistory)





```mermaid
 classDiagram
    class EmploymentHistory
    click EmploymentHistory href "../EmploymentHistory/"
      Professional <|-- EmploymentHistory
        click Professional href "../Professional/"
      

      EmploymentHistory <|-- CurrentEmployment
        click CurrentEmployment href "../CurrentEmployment/"
      EmploymentHistory <|-- PastEmployment
        click PastEmployment href "../PastEmployment/"
      

      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **EmploymentHistory**
            * [CurrentEmployment](CurrentEmployment.md)
            * [PastEmployment](PastEmployment.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:EmploymentHistory](https://w3id.org/lmodel/dpv/pd/EmploymentHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Employment History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#EmploymentHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:EmploymentHistory |
| native | pd:EmploymentHistory |
| exact | dpv_pd:EmploymentHistory, dpv_pd_owl:EmploymentHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EmploymentHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmploymentHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about employment history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Employment History
exact_mappings:
- dpv_pd:EmploymentHistory
- dpv_pd_owl:EmploymentHistory
is_a: Professional
class_uri: pd:EmploymentHistory

```
</details>

### Induced

<details>
```yaml
name: EmploymentHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#EmploymentHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about employment history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Employment History
exact_mappings:
- dpv_pd:EmploymentHistory
- dpv_pd_owl:EmploymentHistory
is_a: Professional
class_uri: pd:EmploymentHistory

```
</details></div>