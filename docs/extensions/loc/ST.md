---
search:
  boost: 10.0
---

# Class: ST 


_Concept representing Country of Sao Tome and Principe_



<div data-search-exclude markdown="1">



URI: [loc:ST](https://w3id.org/lmodel/dpv/loc/ST)





```mermaid
 classDiagram
    class ST
    click ST href "../ST/"
      ST <|-- ST04
        click ST04 href "../ST04/"
      ST <|-- ST05
        click ST05 href "../ST05/"
      ST <|-- STP
        click STP href "../STP/"
      
      
```





## Inheritance
* **ST**
    * [ST04](ST04.md)
    * [ST05](ST05.md)
    * [STP](STP.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ST](https://w3id.org/lmodel/dpv/loc/ST) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Sao Tome and Principe




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ST |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ST |
| native | loc:ST |
| exact | dpv_loc:ST, dpv_loc_owl:ST |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ST
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Sao Tome and Principe
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Sao Tome and Principe
exact_mappings:
- dpv_loc:ST
- dpv_loc_owl:ST
class_uri: loc:ST

```
</details>

### Induced

<details>
```yaml
name: ST
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ST
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Sao Tome and Principe
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Sao Tome and Principe
exact_mappings:
- dpv_loc:ST
- dpv_loc_owl:ST
class_uri: loc:ST

```
</details></div>