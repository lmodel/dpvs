---
search:
  boost: 10.0
---

# Class: Dialect 


_Information about linguistic dialects_



<div data-search-exclude markdown="1">



URI: [pd:Dialect](https://w3id.org/lmodel/dpv/pd/Dialect)





```mermaid
 classDiagram
    class Dialect
    click Dialect href "../Dialect/"
      Language <|-- Dialect
        click Language href "../Language/"
      
      
```





## Inheritance
* [External](External.md)
    * [Language](Language.md)
        * **Dialect**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Dialect](https://w3id.org/lmodel/dpv/pd/Dialect) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Dialect




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Dialect |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Dialect |
| native | pd:Dialect |
| exact | dpv_pd:Dialect, dpv_pd_owl:Dialect |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Dialect
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Dialect
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about linguistic dialects
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Dialect
exact_mappings:
- dpv_pd:Dialect
- dpv_pd_owl:Dialect
is_a: Language
class_uri: pd:Dialect

```
</details>

### Induced

<details>
```yaml
name: Dialect
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Dialect
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about linguistic dialects
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Dialect
exact_mappings:
- dpv_pd:Dialect
- dpv_pd_owl:Dialect
is_a: Language
class_uri: pd:Dialect

```
</details></div>