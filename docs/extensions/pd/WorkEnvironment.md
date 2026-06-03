---
search:
  boost: 10.0
---

# Class: WorkEnvironment 


_Information about work environments_



<div data-search-exclude markdown="1">



URI: [pd:WorkEnvironment](https://w3id.org/lmodel/dpv/pd/WorkEnvironment)





```mermaid
 classDiagram
    class WorkEnvironment
    click WorkEnvironment href "../WorkEnvironment/"
      Professional <|-- WorkEnvironment
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **WorkEnvironment**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:WorkEnvironment](https://w3id.org/lmodel/dpv/pd/WorkEnvironment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Work Environment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#WorkEnvironment |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:WorkEnvironment |
| native | pd:WorkEnvironment |
| exact | dpv_pd:WorkEnvironment, dpv_pd_owl:WorkEnvironment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkEnvironment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#WorkEnvironment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about work environments
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Work Environment
exact_mappings:
- dpv_pd:WorkEnvironment
- dpv_pd_owl:WorkEnvironment
is_a: Professional
class_uri: pd:WorkEnvironment

```
</details>

### Induced

<details>
```yaml
name: WorkEnvironment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#WorkEnvironment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about work environments
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Work Environment
exact_mappings:
- dpv_pd:WorkEnvironment
- dpv_pd_owl:WorkEnvironment
is_a: Professional
class_uri: pd:WorkEnvironment

```
</details></div>