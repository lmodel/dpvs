---
search:
  boost: 10.0
---

# Class: CurrentEmployment 


_Information about current employment_



<div data-search-exclude markdown="1">



URI: [pd:CurrentEmployment](https://w3id.org/lmodel/dpv/pd/CurrentEmployment)





```mermaid
 classDiagram
    class CurrentEmployment
    click CurrentEmployment href "../CurrentEmployment/"
      EmploymentHistory <|-- CurrentEmployment
        click EmploymentHistory href "../EmploymentHistory/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * [EmploymentHistory](EmploymentHistory.md)
            * **CurrentEmployment**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CurrentEmployment](https://w3id.org/lmodel/dpv/pd/CurrentEmployment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Current Employment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CurrentEmployment |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CurrentEmployment |
| native | pd:CurrentEmployment |
| exact | dpv_pd:CurrentEmployment, dpv_pd_owl:CurrentEmployment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CurrentEmployment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CurrentEmployment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about current employment
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Current Employment
exact_mappings:
- dpv_pd:CurrentEmployment
- dpv_pd_owl:CurrentEmployment
is_a: EmploymentHistory
class_uri: pd:CurrentEmployment

```
</details>

### Induced

<details>
```yaml
name: CurrentEmployment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CurrentEmployment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about current employment
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Current Employment
exact_mappings:
- dpv_pd:CurrentEmployment
- dpv_pd_owl:CurrentEmployment
is_a: EmploymentHistory
class_uri: pd:CurrentEmployment

```
</details></div>