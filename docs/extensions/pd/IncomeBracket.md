---
search:
  boost: 10.0
---

# Class: IncomeBracket 


_Information about income bracket_



<div data-search-exclude markdown="1">



URI: [pd:IncomeBracket](https://w3id.org/lmodel/dpv/pd/IncomeBracket)





```mermaid
 classDiagram
    class IncomeBracket
    click IncomeBracket href "../IncomeBracket/"
      Demographic <|-- IncomeBracket
        click Demographic href "../Demographic/"
      
      
```





## Inheritance
* [External](External.md)
    * [Demographic](Demographic.md)
        * **IncomeBracket**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:IncomeBracket](https://w3id.org/lmodel/dpv/pd/IncomeBracket) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Income Bracket




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#IncomeBracket |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:IncomeBracket |
| native | pd:IncomeBracket |
| exact | dpv_pd:IncomeBracket, dpv_pd_owl:IncomeBracket |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IncomeBracket
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IncomeBracket
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about income bracket
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Income Bracket
exact_mappings:
- dpv_pd:IncomeBracket
- dpv_pd_owl:IncomeBracket
is_a: Demographic
class_uri: pd:IncomeBracket

```
</details>

### Induced

<details>
```yaml
name: IncomeBracket
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IncomeBracket
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about income bracket
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Income Bracket
exact_mappings:
- dpv_pd:IncomeBracket
- dpv_pd_owl:IncomeBracket
is_a: Demographic
class_uri: pd:IncomeBracket

```
</details></div>