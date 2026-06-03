---
search:
  boost: 10.0
---

# Class: Nationality 


_Information about nationality_



<div data-search-exclude markdown="1">



URI: [pd:Nationality](https://w3id.org/lmodel/dpv/pd/Nationality)





```mermaid
 classDiagram
    class Nationality
    click Nationality href "../Nationality/"
      External <|-- Nationality
        click External href "../External/"
      
      
```





## Inheritance
* [External](External.md)
    * **Nationality**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Nationality](https://w3id.org/lmodel/dpv/pd/Nationality) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Nationality




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Nationality |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Nationality |
| native | pd:Nationality |
| exact | dpv_pd:Nationality, dpv_pd_owl:Nationality |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Nationality
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Nationality
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about nationality
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Nationality
exact_mappings:
- dpv_pd:Nationality
- dpv_pd_owl:Nationality
is_a: External
class_uri: pd:Nationality

```
</details>

### Induced

<details>
```yaml
name: Nationality
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Nationality
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about nationality
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Nationality
exact_mappings:
- dpv_pd:Nationality
- dpv_pd_owl:Nationality
is_a: External
class_uri: pd:Nationality

```
</details></div>