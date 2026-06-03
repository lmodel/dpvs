---
search:
  boost: 10.0
---

# Class: AT 


_Concept representing Country of Austria_



<div data-search-exclude markdown="1">



URI: [loc:AT](https://w3id.org/lmodel/dpv/loc/AT)





```mermaid
 classDiagram
    class AT
    click AT href "../AT/"
      EEA30 <|-- AT
        click EEA30 href "../EEA30/"
      EEA31 <|-- AT
        click EEA31 href "../EEA31/"
      EU <|-- AT
        click EU href "../EU/"
      EU27 <|-- AT
        click EU27 href "../EU27/"
      EU28 <|-- AT
        click EU28 href "../EU28/"
      EEA <|-- AT
        click EEA href "../EEA/"
      

      AT <|-- AT1
        click AT1 href "../AT1/"
      AT <|-- AT2
        click AT2 href "../AT2/"
      AT <|-- AT3
        click AT3 href "../AT3/"
      AT <|-- AT4
        click AT4 href "../AT4/"
      AT <|-- AT5
        click AT5 href "../AT5/"
      AT <|-- AT6
        click AT6 href "../AT6/"
      AT <|-- AT7
        click AT7 href "../AT7/"
      AT <|-- AT8
        click AT8 href "../AT8/"
      AT <|-- AT9
        click AT9 href "../AT9/"
      

      
```





## Inheritance
* [EEA](EEA.md)
    * **AT** [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * [AT1](AT1.md)
        * [AT2](AT2.md)
        * [AT3](AT3.md)
        * [AT4](AT4.md)
        * [AT5](AT5.md)
        * [AT6](AT6.md)
        * [AT7](AT7.md)
        * [AT8](AT8.md)
        * [AT9](AT9.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AT](https://w3id.org/lmodel/dpv/loc/AT) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Austria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AT |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AT |
| native | loc:AT |
| exact | dpv_loc:AT, dpv_loc_owl:AT |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Austria
exact_mappings:
- dpv_loc:AT
- dpv_loc_owl:AT
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:AT

```
</details>

### Induced

<details>
```yaml
name: AT
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Austria
exact_mappings:
- dpv_loc:AT
- dpv_loc_owl:AT
is_a: EEA
mixins:
- EEA30
- EEA31
- EU
- EU27
- EU28
class_uri: loc:AT

```
</details></div>