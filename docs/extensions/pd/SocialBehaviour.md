---
search:
  boost: 10.0
---

# Class: SocialBehaviour 


_Information about social behaviour(s)_



<div data-search-exclude markdown="1">



URI: [pd:SocialBehaviour](https://w3id.org/lmodel/dpv/pd/SocialBehaviour)





```mermaid
 classDiagram
    class SocialBehaviour
    click SocialBehaviour href "../SocialBehaviour/"
      Social <|-- SocialBehaviour
        click Social href "../Social/"
      Behavioural <|-- SocialBehaviour
        click Behavioural href "../Behavioural/"
      
      
```





## Inheritance
* [External](External.md)
    * [Behavioural](Behavioural.md)
        * **SocialBehaviour** [ [Social](Social.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:SocialBehaviour](https://w3id.org/lmodel/dpv/pd/SocialBehaviour) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Social Behaviour




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#SocialBehaviour |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:SocialBehaviour |
| native | pd:SocialBehaviour |
| exact | dpv_pd:SocialBehaviour, dpv_pd_owl:SocialBehaviour |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SocialBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social behaviour(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Behaviour
exact_mappings:
- dpv_pd:SocialBehaviour
- dpv_pd_owl:SocialBehaviour
is_a: Behavioural
mixins:
- Social
class_uri: pd:SocialBehaviour

```
</details>

### Induced

<details>
```yaml
name: SocialBehaviour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#SocialBehaviour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about social behaviour(s)
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Social Behaviour
exact_mappings:
- dpv_pd:SocialBehaviour
- dpv_pd_owl:SocialBehaviour
is_a: Behavioural
mixins:
- Social
class_uri: pd:SocialBehaviour

```
</details></div>